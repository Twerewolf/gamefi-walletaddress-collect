# gamefi-walletaddress-collect
通过footprint获取gamefi transactions
https://docs.footprint.network/reference/get_protocol-transactions

## pprint
pprint is a package, we use it as pprint.pprint(object) to print sth.

## need to Categorize all contract addresses.
We use some Alchemy APIs to check ERC20/721/1155. Other types just set as 'Unknown' or do not set.  
1. Get erc20 type from token totalsupply query api in footprint api v2 (the data is not 100% correct)
2. Get erc721/erc1155 from bacscan web. Use curl
3. The erc20 type info in 1. need to be fixed. Consider the method in 2. we get the contract's bscscan web to see the classification.