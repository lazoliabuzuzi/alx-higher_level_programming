#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

#define MAX_SIZE 100

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pinter to pointer of first node in list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current;
	int count;
	int val[MAX_SIZE];
	int start, end;

	if (head == NULL || (*head)->next == NULL)
		return (1);

	current = *head;

	while (current != NULL)
	{
		val[count] = current->n;
		current = current->next;
		count++;
	}

	start = 0;
	end = count - 1;

	while (start < end)
	{
		if (val[start] != val[end])
		{
			return (0);
		}
		start++;
		end--;
	}

	return (1);
}
