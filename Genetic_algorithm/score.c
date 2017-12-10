#include"Python.h"

long idx;

double scoreMe(PyObject* args){ 
    PyObject* allSpec;
    PyObject* art;
    PyObject* final_score;
    int W=0,H=0;
    double sc = 0.0;
    int idx;

    if (! PyArg_ParseTuple( args, "OiiiO", &allSpec, &W, &H, &idx, &art))
        return -1;
    
    PyObject* tmp = PyList_GetItem(allSpec, idx);

    for(int j = 0; j<H;j++){
        for(int i = 0; i< W; i++){
            long a = PyLong_AsLong(PyList_GetItem(tmp, j * W + i));
            long b = PyLong_AsLong(PyList_GetItem(art, j * W + i));
            sc += (a-b) * (a-b);
        }
    }
    return PyLong_AsLong(Py_BuildValue("d", sc));
}

double res;
static PyObject* scoreFunc_score(PyObject* self, PyObject* args){
    PyObject* specimensList; //lista wszystkich osobników (fitness)
    PyObject* allSpec;
    PyObject* art;
    int W=0, H=0;

    if (! PyArg_ParseTuple( args, "OiiOO", &specimensList, &W, &H, &allSpec, &art))
        return NULL;
    
    long specimen_lenght = PyList_Size(specimensList);
    
    for(int i = 0; i < specimen_lenght; i++){
        PyObject* tmp = PyList_GetItem(specimensList, i);
        PyObject* m = Py_BuildValue("i", i);
        PyObject_SetAttrString(tmp, "idx", m);
        PyObject* ob2 = PyObject_GetAttrString(tmp, "idx");
        idx = PyLong_AsLong(ob2);
        
        PyObject* args_sM2 = Py_BuildValue("OiiiO", allSpec, W, H, idx, art);
        res = scoreMe(args_sM2);
        PyObject* set = Py_BuildValue("d", res);
        PyObject_SetAttrString(tmp, "fitness_score", set);
        PyObject* fitt = PyObject_GetAttrString(tmp, "fitness_score");
        long fit = PyLong_AsLong(fitt);
        
    }
    return Py_None;
}

static PyObject* bestOnes(PyObject *self, PyObject* args){
    PyObject* bestList;
    PyObject* fitness;
    int best_cnt;
    
    if(!PyArg_ParseTuple(args, "OOi", &bestList, &fitness, &best_cnt))
        return -1;

    for(int i = 0; i<best_cnt; i++){
        PyObject* tmp = PyList_GetItem(fitness, i);
        int idx = PyLong_AsLong(PyObject_GetAttrString(tmp, "idx"));
        //printf("%i ", idx);
        PyObject* index = Py_BuildValue("i", idx);
        PyList_SetItem(bestList, i, index);
    }

    return Py_None;
}

static PyMethodDef score_funcs[] = {
    {"score", (PyCFunction)scoreFunc_score, METH_VARARGS, "score the specimens"},
    {"score_me", (PyCFunction)scoreMe, METH_VARARGS, "score the specimens"},
    {"best_ones", (PyCFunction)bestOnes, METH_VARARGS, "fill the list of best specimens from current generation"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef score =
{
    PyModuleDef_HEAD_INIT,
    "score", /* name of module */
    "score(list of Specimens, list of best values)", /* module documentation, may be NULL */
    -1,   /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
    score_funcs
};

PyMODINIT_FUNC PyInit_score(void)
{
    return PyModule_Create(&score);
}

