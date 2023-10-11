#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes = (PyBytesObject *)p;

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", PyBytes_Size(p));
    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first 10 bytes:");
    for (Py_ssize_t i = 0; i < 10; ++i)
    {
        if (i < PyBytes_Size(p))
            printf(" %02x", (unsigned char)bytes->ob_sval[i]);
        else
            printf(" 00");
    }
    printf("\n");
}

void print_python_list(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
    printf("[*] Allocated = %ld\n", list->allocated);

    for (Py_ssize_t i = 0; i < PyList_Size(p); ++i)
    {
        PyObject *item = PyList_GetItem(p, i);
        const char *type_name = Py_TYPE(item)->tp_name;

        printf("Element %ld: %s\n", i, type_name);
        if (PyBytes_Check(item))
            print_python_bytes(item);
    }
}
