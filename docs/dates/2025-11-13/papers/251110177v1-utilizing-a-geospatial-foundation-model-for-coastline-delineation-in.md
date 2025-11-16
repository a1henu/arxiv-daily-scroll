---
layout: default
title: Utilizing a Geospatial Foundation Model for Coastline Delineation in Small Sandy Islands
---

# Utilizing a Geospatial Foundation Model for Coastline Delineation in Small Sandy Islands
**arXiv**：[2511.10177v1](https://arxiv.org/abs/2511.10177) · [PDF](https://arxiv.org/pdf/2511.10177.pdf)  
**作者**：Tishya Chhabra, Manisha Bajpai, Walter Zesk, Skylar Tibbits  

**一句话要点**：利用Prithvi-EO-2.0地理空间基础模型进行小沙岛海岸线描绘

**关键词**：地理空间基础模型, 海岸线描绘, 小沙岛监测, 多光谱图像, 迁移学习

## 3 点简述
- 核心问题：小沙岛海岸线描绘在数据稀缺区域存在挑战。
- 方法要点：微调Prithvi模型，使用少量多光谱卫星图像进行训练。
- 实验效果：仅5张训练图像即可实现高F1和IoU分数。

## 摘要（原文）

> We present an initial evaluation of NASA and IBM's Prithvi-EO-2.0 geospatial foundation model on shoreline delineation of small sandy islands using satellite images. We curated and labeled a dataset of 225 multispectral images of two Maldivian islands, which we publicly release, and fine-tuned both the 300M and 600M parameter versions of Prithvi on training subsets ranging from 5 to 181 images. Our experiments show that even with as few as 5 training images, the models achieve high performance (F1 of 0.94, IoU of 0.79). Our results demonstrate the strong transfer learning capability of Prithvi, underscoring the potential of such models to support coastal monitoring in data-poor regions.

