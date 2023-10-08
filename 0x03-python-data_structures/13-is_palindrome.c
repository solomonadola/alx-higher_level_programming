#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int len = 0, i = 0;
	int arr[100000];

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (current != NULL)
	{
		arr[len] = current->n;
		len++;
		current = current->next;
	}
	for (i = 0; i < len / 2; i++)
	{
		if (arr[i] != arr[len - i - 1])
			return (0);
	}
	return (1);
}
