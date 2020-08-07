#include <iostream>
using namespace std;

class node
{
public:
    int data;
    node *next;
};

node *newnode(int data)
{
    node *t=new node();
    t->data=data;
    t->next=NULL;
    return t;
}

int length(node *head)
{
    int l=0;
    while(head)
    {
        l=l+1;
        head=head->next;
    }
    return l;
}

void intersection(node *h1,node *h2)
{
    int l1=length(h1);
    int l2=length(h2);
    if(h1>=h2)
    {
        int d=l1-l2;
        while(d>0)
        {
            h1=h1->next;
            d=d-1;
        }
        //Here I will consider two linked lists to intersect at a node if they have same data. While condition can be modified to h1!=h2 instead of h1->data!=h2->data. This is just for demo purposes...
        while(h1->data!=h2->data)
        {
            h1=h1->next;
            h2=h2->next;
        }
        cout<<h1->data;
    }
    else
    {
        int d=l2-l1;
        while(d>0)
        {
            h2=h2->next;
            d=d-1;
        }
        while(h1->data!=h2->data)
        {
            h1=h1->next;
            h2=h2->next;
        }
        cout<<h1->data;
    }
}

node *createll(int *arr,int n)
{
    if(n==0)
    {
        return NULL;
    }
    node *h=newnode(arr[0]);
    node *curr=h;
    for (int i=1;i<n;i++)
    {
        curr->next=newnode(arr[i]);
        curr=curr->next;
    }
    curr->next=NULL;
    return h;
}

void traversal(node *h)
{
    while(h)
    {
        cout<<h->data<<" ";
        h=h->next;
    }
}

int main()
{
    int a[5]={3,7,8,10,4};
    int b[6]={23,99,8,10,4};
    node *h1=createll(&a[0],5);
    node *h2=createll(&b[0],6);
    intersection(h1,h2);
}