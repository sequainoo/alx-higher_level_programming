#include "lists.h"

/**
 * is_palindrome - checks if a linked list is pallindrome
 * @head: a pointer to a pointer to a list node
 *
 * Description: calls a recursive function  to check for
 * palindrome
 * Return: 1 if true n 0 if false
 */
int is_palindrome(listint_t **head)
{
	listint_t *right_ptr = NULL, *left_ptr = NULL;
	int left_pos = 0, right_pos = 0;
	int len = list_len(*head);

	if (*head == NULL)
		return (1);

	if (len % 2 != 0)
	{
		left_pos = (len / 2) - 1;
		right_pos = (len / 2) + 1;
	}
	else
	{
		left_pos = (len / 2) - 1;
		right_pos = (len / 2);
	}
	left_ptr = get_node(*head, left_pos);
	right_ptr = get_node(*head, right_pos);

	return (palindrome(*head, left_ptr, right_ptr, left_pos));
}

/**
 * get_node - return a pointer to  a node
 * @head: head of list
 * @pos: position to get
 * Return: a pointer
 */
listint_t *get_node(listint_t *head, int pos)
{
	int i = 0;

	while (head != NULL)
	{
		if (i == pos)
			return (head);
		head = head->next;
		i += i;
	}
	return (NULL);
}

/**
 * list_len - checks the length of a singly linked list
 * @head: a pointer to head of list
 * Return: an integer
 */
int list_len(listint_t *head)
{
	if (head->next == NULL)
		return (1);
	return (1 + list_len(head->next));
}

/**
 * palindrome_check - recursively compares list in diverging path from center
 * @head: head of list
 * @l_ptr: a pointer that will be moving left
 * @r_ptr: a pointer moving right
 * @l_pos: position of the current left_pointer
 *
 * Description: moves positions in diverging ways
 * Return: 1 for palindrome and 0 for false
 */
int palindrome(listint_t *head, listint_t *l_ptr, listint_t *r_ptr, int l_pos)
{
	if (r_ptr == NULL)
		return (1);
	if (l_ptr->n != r_ptr->n)
		return (0);

	l_ptr = get_node(head, --l_pos);
	return (palindrome(head, l_ptr, r_ptr->next, l_pos));
}
