#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of first node in list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *prev = NULL; 
	listint_t *snail = *head;
	listint_t *hare = *head;
	listint_t *next;

	if (head == NULL || (*head)->next == NULL)
		return (1);

	snail = *head;
	hare = *head;

	while (hare != NULL && hare->next != NULL)
	{
		hare = hare->next->next;
		next = snail->next;
		snail->next = prev;
		prev = snail;
		snail = next;
	}

	if (hare != NULL)
		snail = snail->next;

	while (snail != NULL)
	{
		if (prev->n != snail->n)
		{
			return (0);
		}
		prev = prev->next;
		snail = snail->next;
	}

	return (1);
}

