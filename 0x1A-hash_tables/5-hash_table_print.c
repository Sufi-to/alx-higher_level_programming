#include "hash_tables.h"
/**
 * hash_table_print - prints the hash table elements
 * @ht: hash table to be printed
 * Return: None
*/
void hash_table_print(const hash_table_t *ht)
{
	unsigned long int size;
	unsigned long int i;
	hash_node_t *item;
	unsigned long int h;

	h = 0;
	if (ht == NULL)
		return;
	size = ht->size;
	printf("{");
	for (i = 0; i < size; i++)
	{
		item = ht->array[i];
		while (item != NULL)
		{
			if (h) /*
					* h is 0 until we find the first element after that it will be making
					* the loop print , after each node and when it reaches the last
					* since there is nothing after it the loop will not execute and
					* the comma will not be printed.
					*/
				printf(", ");
			printf("'%s': '%s'", item->key, item->value);
			item = item->next;
			h = 1;
		}
	}
	printf("}\n");
}
