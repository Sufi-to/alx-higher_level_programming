#include "hash_tables.h"
/**
 * key_index - calculates the index of the hash_node to be added
 * to on the hash_table
 * @key: key on which the hash function will be applied on
 * @size: size of the hash_table
 * Return: index of the key on the hash_table
*/
unsigned long int key_index(const unsigned char *key, unsigned long int size)
{
	return (hash_djb2(key) % size);
}
