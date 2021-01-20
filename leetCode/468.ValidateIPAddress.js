/**
 * @param {string} IP
 * @return {string}
 */

 const isDigit = (char) => '0' <= char && char <= '9'
 const isAlphabet = (char) => ('a' <= char && char <= 'f') || ('A' <= char && char <= 'F')

const isIPv4 = (IP) => {
  if (IP.indexOf('.') < 1) return false

  const digits = IP.split('.')
  if (digits.length !== 4) return false

  for (let i = 0; i < digits.length; i++) {
    const digit = digits[i]
    if (digit.length == 0) return false
    if (digit[0] == '0' && digit.length > 1) return false
    for (let j = 0; j < digit.length; j++) {
      if (!isDigit(digit[j])) return false
    }
    
    const parsedDigit = parseInt(digit)
    if (0 > parsedDigit || parsedDigit > 255) return false
  }
  return true
}

const isIPv6 = (IP) => {
  if (IP.indexOf(':') < 1) return false

  const hexadecimals = IP.split(':')
  if (hexadecimals.length !== 8) return false

  for (let i = 0; i < hexadecimals.length; i++) {
    const hexadecimal = hexadecimals[i]
    if (hexadecimal.length == 0 || hexadecimal.length > 4) return false
    for (let j = 0; j < hexadecimal.length; j++) {
      const char = hexadecimal[j]
      if (!(isDigit(char) || isAlphabet(char))) return false
    }
  }
  return true
}

const validIPAddress = (IP) => {
  if (isIPv4(IP)) return 'IPv4'
  if (isIPv6(IP)) return 'IPv6'
  return 'Neither'
}



const IP = '2001:0db8:85a3:0:0:8A2E:0370:7334'

console.log(validIPAddress(IP))