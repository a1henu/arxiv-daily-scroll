---
layout: default
title: Where are the Whales: A Human-in-the-loop Detection Method for Identifying Whales in High-resolution Satellite Imagery
---

# Where are the Whales: A Human-in-the-loop Detection Method for Identifying Whales in High-resolution Satellite Imagery
**arXiv**：[2510.14709v1](https://arxiv.org/abs/2510.14709) · [PDF](https://arxiv.org/pdf/2510.14709.pdf)  
**作者**：Caleb Robinson, Kimberly T. Goetz, Christin B. Khan, Meredith Sackett, Kathleen Leonard, Rahul Dodhia, Juan M. Lavista Ferres  

**一句话要点**：提出半自动化方法以识别高分辨率卫星图像中的鲸鱼，结合异常检测与专家标注。

**关键词**：鲸鱼检测, 卫星图像分析, 异常检测, 半自动化方法, 海洋哺乳动物监测

## 3 点简述
- 核心问题：传统鲸鱼监测方法成本高、难扩展，自动化检测面临标注数据少、图像质量多变等挑战。
- 方法要点：使用统计异常检测标记空间异常点，并开发基于Web的标注界面供专家快速验证。
- 实验效果：在三个基准场景中，召回率达90.3%至96.4%，专家检查面积减少高达99.8%。

## 摘要（原文）

> Effective monitoring of whale populations is critical for conservation, but
> traditional survey methods are expensive and difficult to scale. While prior
> work has shown that whales can be identified in very high-resolution (VHR)
> satellite imagery, large-scale automated detection remains challenging due to a
> lack of annotated imagery, variability in image quality and environmental
> conditions, and the cost of building robust machine learning pipelines over
> massive remote sensing archives. We present a semi-automated approach for
> surfacing possible whale detections in VHR imagery using a statistical anomaly
> detection method that flags spatial outliers, i.e. "interesting points". We
> pair this detector with a web-based labeling interface designed to enable
> experts to quickly annotate the interesting points. We evaluate our system on
> three benchmark scenes with known whale annotations and achieve recalls of
> 90.3% to 96.4%, while reducing the area requiring expert inspection by up to
> 99.8% -- from over 1,000 sq km to less than 2 sq km in some cases. Our method
> does not rely on labeled training data and offers a scalable first step toward
> future machine-assisted marine mammal monitoring from space. We have open
> sourced this pipeline at https://github.com/microsoft/whales.

