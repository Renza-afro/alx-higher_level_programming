#include "lists.h"

/**
* is_palindrome-> checks if singly linked list is palindrome
* @head: ptr
* Return: 0 if not palindrome. 1 if is palindrome
*/
int is_palindrome(listint_t **head)
{
int list[1000000], x = 0, y = 0, z = 0;
listint_t *tmp;

if (head == NULL || (*head) == NULL)
return (1);
tmp = *head;
while (tmp)
{
list[x] = tmp->n;
x++;
tmp = tmp->next;
}
x--;
if (x % 2 != 0)
z = (x + 1) / 2;
else
z = x / 2;
while (y < z)
{
if (list[y] != list[x])
return (0);
x--;
y++;
}
return (1);
}
