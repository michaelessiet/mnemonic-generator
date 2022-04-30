import { utils } from "ethers"

export default function mnemonicCheck({ query: { phrase } }, res) {
  const isValid = utils.isValidMnemonic(phrase)

  if (isValid) {
    res.status(200).json({ isValid })
  } else {
    res.status(200).json({ isValid })
  }
}