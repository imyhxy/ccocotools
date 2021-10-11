## Fast COCOApi for `bbox` task

This repository just copy and paste [PythonAPI](https://github.com/cocodataset/cocoapi) from the
official [cocoapi](https://github.com/cocodataset/cocoapi/tree/master/PythonAPI), merge the C++ implementation
of [`COCOeval`](https://github.com/facebookresearch/detectron2/tree/main/detectron2/layers/csrc)
in [detectron2](https://github.com/facebookresearch/detectron2)
into [`FastCOCOeval`](https://github.com/imyhxy/ccocotools/tree/main/ccocotools/). Simplify all unnecessary
requirements and make it easy to install.

### Installation

* Install from local:

    ```bash
    git clone https://github.com/imyhxy/ccocotools
    cd ccocotools && python setup.py install
    ```

* Install from Github:

    ```bash
    pip install git+http://github.com/imyhxy/ccocotools
    ```

### Usage

```python
from ccocotools.coco import COCO
from ccocotools.fastcocoeval import FastCOCOeval

gt_json = 'instance_val2017.json'
pd_json = 'predictions.json'

anno = COCO(gt_json)
pred = anno.loadRes(pd_json)
coco_eval = FastCOCOeval(anno, pred, 'bbox')
coco_eval.evaluate()
coco_eval.accumulate()
coco_eval.summarize()
```

### Performance

The C++ implementation reduces 75% total time compares to the python one.

|Implementation|`evaluate()`|`accumulate()`|`summarize()`|Total|
|:---|---:|---:|---:|---:|
|Python|73.0s|15.4s|3.6ms|92.0s|
|C++|16.4s|2.5s|3.9ms|22.8s|

### Reference

1. [COCOApi](https://github.com/cocodataset/cocoapi)
2. [Detectron2](https://github.com/facebookresearch/detectron2)