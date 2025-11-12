---
layout: default
title: Perceptual Quality Assessment of 3D Gaussian Splatting: A Subjective Dataset and Prediction Metric
---

# Perceptual Quality Assessment of 3D Gaussian Splatting: A Subjective Dataset and Prediction Metric
**arXiv**：[2511.08032v1](https://arxiv.org/abs/2511.08032) · [PDF](https://arxiv.org/pdf/2511.08032.pdf)  
**作者**：Zhaolin Wan, Yining Diao, Jingqi Xu, Hao Wang, Zhiyang Li, Xiaopeng Fan, Wangmeng Zuo, Debin Zhao  

**一句话要点**：提出3DGS-QA数据集与无参考质量预测模型，以评估3D高斯泼溅的感知质量。

**关键词**：3D高斯泼溅, 感知质量评估, 无参考质量预测, 主观数据集, 3D渲染失真

## 3 点简述
- 核心问题：3D高斯泼溅渲染内容在多种失真因素下的感知质量未被系统研究。
- 方法要点：构建主观数据集并开发基于高斯原语的无参考质量预测模型。
- 实验或效果：模型在基准测试中表现优越，数据集和代码已公开。

## 摘要（原文）

> With the rapid advancement of 3D visualization, 3D Gaussian Splatting (3DGS) has emerged as a leading technique for real-time, high-fidelity rendering. While prior research has emphasized algorithmic performance and visual fidelity, the perceptual quality of 3DGS-rendered content, especially under varying reconstruction conditions, remains largely underexplored. In practice, factors such as viewpoint sparsity, limited training iterations, point downsampling, noise, and color distortions can significantly degrade visual quality, yet their perceptual impact has not been systematically studied. To bridge this gap, we present 3DGS-QA, the first subjective quality assessment dataset for 3DGS. It comprises 225 degraded reconstructions across 15 object types, enabling a controlled investigation of common distortion factors. Based on this dataset, we introduce a no-reference quality prediction model that directly operates on native 3D Gaussian primitives, without requiring rendered images or ground-truth references. Our model extracts spatial and photometric cues from the Gaussian representation to estimate perceived quality in a structure-aware manner. We further benchmark existing quality assessment methods, spanning both traditional and learning-based approaches. Experimental results show that our method consistently achieves superior performance, highlighting its robustness and effectiveness for 3DGS content evaluation. The dataset and code are made publicly available at https://github.com/diaoyn/3DGSQA to facilitate future research in 3DGS quality assessment.

