#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *bytes_object)
{
    long int size;
    int i;
    char *data = NULL;

    printf("[.] Bytes object info\n");
    if (!PyBytes_Check(bytes_object))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    PyBytes_AsStringAndSize(bytes_object, &data, &size);

    printf("  Size: %li\n", size);
    printf("  Data: %s\n", data);
    if (size < 10)
        printf("  First %li bytes:", size + 1);
    else
        printf("  First 10 bytes:");
        
    for (i = 0; i <= size && i < 10; i++)
        printf(" %02hhx", data[i]);

    printf("\n");
}

void print_python_list(PyObject *list_object)
{
    long int size = PyList_Size(list_object);
    int i;
    PyListObject *list = (PyListObject *)list_object;
    const char *element_type;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List: %li\n", size);
    printf("[*] Allocated memory: %li\n", list->allocated);

    for (i = 0; i < size; i++)
    {
        element_type = (list->ob_item[i])->ob_type->tp_name;
        printf("Element %i: %s\n", i, element_type);
        
        if (!strcmp(element_type, "bytes"))
            print_python_bytes(list->ob_item[i]);
    }
}
