#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to head of singly linked list
 *
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (!head || !(*head))
	{
		return (1);
	}

	listint_t *slow = *head, *fast = *head, *prev = NULL, *temp = NULL;

	while (fast && fast->next)
	{
		fast = fast->next->next;
		temp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = temp;
	}

	if (fast)
	{
		slow = slow->next;
	}

	while (slow)
	{
		if (slow->n != prev->n)
		{
			return (0);
		}
		slow = slow->next;
		prev = prev->next;
	}

	return (1);
}
