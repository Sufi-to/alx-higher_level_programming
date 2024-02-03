#include "hash_tables.h"
/**
 * hash_table_set - sets the hash_table with an element
 * @ht: hash table
 * @key: information to be stored as key of the node in the hash table
 * @value: value of the key
 * Return: 0 if it faile or 1 if it succeeds
*/
int hash_table_set(hash_table_t *ht, const char *key, const char *value)
{
	unsigned long int index;
	char *val_cpy;
	hash_node_t *node;
	unsigned long int i;

	if (ht == NULL || key == NULL || *key == '\0' || value == NULL)
		return (0);
	val_cpy = strdup(value);
	if (val_cpy == NULL)
		return (0);
	for (i = 0; ht->array[i]; i++)
	{
		if (strcmp(ht->array[i]->key, key) == 0)
		{
			free(ht->array[i]->value);
			ht->array[i]->value = val_cpy;
			return (1);
		}
	}
	index = key_index((const unsigned char *)key, ht->size);
	node = malloc(sizeof(hash_node_t));
	if (node == NULL)
	{
		free(val_cpy);
		return (0);
	}
	node->key = strdup(key);
	if (node->key == NULL)
	{
		free(node);
		return (0);
	}
	node->value = val_cpy;
	node->next = ht->array[index];
	ht->array[index] = node;
	return (1);
}

