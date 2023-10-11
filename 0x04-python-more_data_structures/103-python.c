#include <Python.h>

void print_python_list(PyObject *p)
{
    long int size, i;
    PyListObject *list;

    printf("[*] Python list info\n");
    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    list = (PyListObject *)p;
    size = PyList_Size(p);

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; i++)
        printf("Element %ld: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
}

void print_python_bytes(PyObject *p)
{
    long int size, i;
    char *str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);
    
    if (size < 10)
        printf("  first %ld bytes:", size + 1);
    else
        printf("  first 10 bytes:");

    for (i = 0; i < size + 1 && i < 10; i++)
        printf(" %02hhx", str[i]);

    printf("\n");
}

