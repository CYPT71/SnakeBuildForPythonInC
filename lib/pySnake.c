#include "snake/play.h"
#include <stdio.h>
#include <Python.h>


static PyObject *method_play(PyObject *self, PyObject *args) 
{
    
    int best, score;

    /* Parse arguments */
    if(!PyArg_ParseTuple(args, "i", &best)) {
        return NULL;
    }
    
    play(best, &best, &score);



    PyObject* MyTuple = PyTuple_New(2);
    PyObject* Best = PyLong_FromLong(best);
    PyObject* Score = PyLong_FromLong(score);

    PyTuple_SetItem(MyTuple, 0, Best);
    PyTuple_SetItem(MyTuple, 1, Score);

    return MyTuple;
}

static PyMethodDef PlayMethods[] = {
    {"play", method_play, METH_VARARGS, "A pure Python snake console game"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef playmodule = {
    PyModuleDef_HEAD_INIT,
    "play",
    "A pure Python snake console game",
    -1,
    PlayMethods
};

PyMODINIT_FUNC PyInit_snake(void) {
    return PyModule_Create(&playmodule);
}
