#include "hash_tables.h"
/**
 * hash_table_create - create a hash table
 * @size: size of the hash table to be created
 * Return: pointer to the hash table created
*/
hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *table;

	table = malloc(sizeof(hash_table_t));
	if (table == NULL)
		return (NULL);

	table->array = malloc(size * sizeof(hash_node_t *));
	if (table->array == NULL)
	{
		free(table);
		return (NULL);
	}
	table->size = size;

	return (table);
}
