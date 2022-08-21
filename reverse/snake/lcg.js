// Paste your JavaScript code here
var lcg_a = 75;
var lcg_c = 74;
var lcg_m = 65537;
var lcg_x = 73;
function lcg() {
  let old_x = lcg_x;
  lcg_x = (lcg_x * lcg_a + lcg_c) % lcg_m;
  return old_x;
}