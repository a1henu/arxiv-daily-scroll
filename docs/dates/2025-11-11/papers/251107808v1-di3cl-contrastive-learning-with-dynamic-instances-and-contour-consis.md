---
layout: default
title: DI3CL: Contrastive Learning With Dynamic Instances and Contour Consistency for SAR Land-Cover Classification Foundation Model
---

# DI3CL: Contrastive Learning With Dynamic Instances and Contour Consistency for SAR Land-Cover Classification Foundation Model
**arXiv**：[2511.07808v1](https://arxiv.org/abs/2511.07808) · [PDF](https://arxiv.org/pdf/2511.07808.pdf)  
**作者**：Zhongle Ren, Hui Ding, Kai Wang, Biao Hou, Xingyu Luo, Weibin Li, Licheng Jiao  

**一句话要点**：提出DI3CL对比学习框架，构建SAR地物分类基础模型以提升泛化能力

**关键词**：SAR地物分类, 对比学习, 基础模型, 轮廓一致性, 动态实例, 泛化能力

## 3 点简述
- 核心问题：监督学习依赖大量标注数据，限制SAR地物分类的泛化与适应性。
- 方法要点：引入动态实例和轮廓一致性模块，增强全局上下文与结构判别。
- 实验效果：在多种任务中优于现有方法，使用大规模数据集提升鲁棒性。

## 摘要（原文）

> Although significant advances have been achieved in SAR land-cover classification, recent methods remain predominantly focused on supervised learning, which relies heavily on extensive labeled datasets. This dependency not only limits scalability and generalization but also restricts adaptability to diverse application scenarios. In this paper, a general-purpose foundation model for SAR land-cover classification is developed, serving as a robust cornerstone to accelerate the development and deployment of various downstream models. Specifically, a Dynamic Instance and Contour Consistency Contrastive Learning (DI3CL) pre-training framework is presented, which incorporates a Dynamic Instance (DI) module and a Contour Consistency (CC) module. DI module enhances global contextual awareness by enforcing local consistency across different views of the same region. CC module leverages shallow feature maps to guide the model to focus on the geometric contours of SAR land-cover objects, thereby improving structural discrimination. Additionally, to enhance robustness and generalization during pre-training, a large-scale and diverse dataset named SARSense, comprising 460,532 SAR images, is constructed to enable the model to capture comprehensive and representative features. To evaluate the generalization capability of our foundation model, we conducted extensive experiments across a variety of SAR land-cover classification tasks, including SAR land-cover mapping, water body detection, and road extraction. The results consistently demonstrate that the proposed DI3CL outperforms existing methods. Our code and pre-trained weights are publicly available at: https://github.com/SARpre-train/DI3CL.

