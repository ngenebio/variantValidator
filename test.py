import VariantValidator
validator = VariantValidator.Validator()


# test = validator.genes_by_region('GRCh38', 'chr17', '48187404-48207246')

test = validator.gene_information('GRCh38', 'NC_000017.11', 'PDK2')

print(test)
