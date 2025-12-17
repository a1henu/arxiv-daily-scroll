---
layout: default
title: Real-time prediction of workplane illuminance distribution for daylight-linked controls using non-intrusive multimodal deep learning
---

# Real-time prediction of workplane illuminance distribution for daylight-linked controls using non-intrusive multimodal deep learning
**arXiv**：[2512.14058v1](https://arxiv.org/abs/2512.14058) · [PDF](https://arxiv.org/pdf/2512.14058.pdf)  
**作者**：Zulin Zhuang, Yu Bian  

**一句话要点**：提出非侵入式多模态深度学习框架，实时预测动态室内工作平面照度分布以支持日光联动控制。

**关键词**：日光联动控制, 工作平面照度预测, 多模态深度学习, 非侵入式图像处理, 实时预测, 时空特征提取

## 3 点简述
- 核心问题：现有室内日光预测研究多针对静态场景，难以适应动态占用空间。
- 方法要点：仅从侧窗区域提取图像时空特征，避免干扰室内像素，实现非侵入式预测。
- 实验或效果：在广州测试室收集17344样本，模型在同分布测试集R2>0.98，未见天测试集R2>0.82，显示高精度与可接受泛化能力。

## 摘要（原文）

> Daylight-linked controls (DLCs) have significant potential for energy savings in buildings, especially when abundant daylight is available and indoor workplane illuminance can be accurately predicted in real time. Most existing studies on indoor daylight predictions were developed and tested for static scenes. This study proposes a multimodal deep learning framework that predicts indoor workplane illuminance distributions in real time from non-intrusive images with temporal-spatial features. By extracting image features only from the side-lit window areas rather than interior pixels, the approach remains applicable in dynamically occupied indoor spaces. A field experiment was conducted in a test room in Guangzhou (China), where 17,344 samples were collected for model training and validation. The model achieved R2 > 0.98 with RMSE < 0.14 on the same-distribution test set and R2 > 0.82 with RMSE < 0.17 on an unseen-day test set, indicating high accuracy and acceptable temporal generalization.

