#include <iostream>
using namespace std;

class node
{
public:
    node *left;
    int data;
    node *right;
    node *parent;
    int locked; //Keeps track of #locked descendants
    bool islocked;
};

bool check(node *root)
{
    return root->islocked;
}

bool lock(node *root,node *p)
{
    if(p->islocked)
    {
        return true;
    }
    if(p==root && p->locked==0)
    {
        p->islocked=true;
        return true;
    }
    if(p==root && p->locked!=0)
    {
        return false;
    }
    if(p->locked==0)
    {
        p->islocked=true;
        node *curr=p;
        while(curr!=root)
        {
            curr=curr->parent;
            curr->locked=curr->locked+1;
        }
        return true;
    }
    node *curr=p;
    while(curr!=root)
    {
        curr=curr->parent;
        if(curr->islocked)
        {
            return false;
        }
    }
    curr=p;
    p->islocked=true;
    while(curr!=root)
    {
        curr=curr->parent;
        curr->locked=curr->locked+1;
    }
    return true;
}

bool unlock(node *p,node *root)
{
    if(!p->islocked)
    {
        return true;
    }
    if(p==root && p->locked==0)
    {
        p->islocked=false;
        return true;
    }
    if(p==root && p->locked!=0)
    {
        return false;
    }
    if(p->locked==0)
    {
        p->islocked=false;
        node *curr=p;
        while(curr!=root)
        {
            curr=curr->parent;
            curr->locked=curr->locked-1;
        }
        return true;
    }
    node *curr=p;
    while(curr!=root)
    {
        curr=curr->parent;
        if(curr->islocked)
        {
            return false;
        }
    }
    p->islocked=false;
    curr=p;
    while(curr!=root)
    {
        curr=curr->parent;
        curr->locked=curr->locked-1;
    }
    return true;
}