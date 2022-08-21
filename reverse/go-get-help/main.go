package main

import (
	"bytes"
	"go/build"
	"io/ioutil"

	"github.com/DavidTan0527/go-get-help/src"
	"golang.org/x/tools/go/packages"
	"golang.org/x/tools/go/ssa"
	"golang.org/x/tools/go/ssa/ssautil"
)

func main() {
	cfg := &packages.Config{
		Mode:       packages.NeedSyntax | packages.NeedTypes | packages.NeedTypesInfo | packages.NeedImports,
		Dir:        "/Users/davidtan/Coding/welcome-ctf-2022/challenges/reverse/go-get-help",
		BuildFlags: build.Default.BuildTags,
	}
	loaded, err := packages.Load(cfg, "github.com/DavidTan0527/go-get-help/src/...")
	if err != nil {
		panic(err)
	}

	prog, _ := ssautil.Packages(loaded, 0)
	// Build SSA code for the whole program.
	prog.Build()
	pkgs := prog.AllPackages()
	var bArr []byte
	b := bytes.NewBuffer(bArr)

	ssa.WritePackage(b, pkgs[0])

	bs, err := ioutil.ReadAll(b)
	if err != nil {
		panic(err)
	}

	ioutil.WriteFile("main.ssa", bs, 0644)

	src.Main()

	// indices := make(map[string][]int)
	// flag := "greyhats{st4t1c_s1nGl3_4ss1Gnm3nt}"
	// for i, c := range flag {
	// 	indices[string(c)] = append(indices[string(c)], i)
	// }

	// for k, v := range indices {
	// 	fmt.Printf("%s: %v\n", k, v)
	// }
}
