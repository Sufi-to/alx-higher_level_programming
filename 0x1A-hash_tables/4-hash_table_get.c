#include "hash_tables.h"
/**
 * hash_table_get - gets the value associated with a given key
 * @ht: the hash table to be searched
 * @key: key by which we will find the value
 * Return: pointer to the value
*/
char *hash_table_get(const hash_table_t *ht, const char *key)
{
	unsigned long int index;
	hash_node_t *item;

	if (ht == NULL || key == NULL || *key == '\0')
		return (0);

	index = key_index((const unsigned char *)key, ht->size);
	item = ht->array[index];
	if (item == NULL)
		return (NULL);

	if (strcmp(item->key, key) != 0)
		return (NULL);

	return (item->value);
}
