---
layout: default
title: Cyberattack Detection in Virtualized Microgrids Using LightGBM and Knowledge-Distilled Classifiers
---

# Cyberattack Detection in Virtualized Microgrids Using LightGBM and Knowledge-Distilled Classifiers
**arXiv**：[2601.03495v1](https://arxiv.org/abs/2601.03495) · [PDF](https://arxiv.org/pdf/2601.03495.pdf)  
**作者**：Osasumwen Cedric Ogiesoba-Eguakun, Suman Rath  

**一句话要点**：提出基于LightGBM和知识蒸馏的轻量级模型，用于虚拟微电网的快速网络攻击检测

**关键词**：微电网网络安全, LightGBM分类, 知识蒸馏, 攻击检测, 虚拟仿真, 边缘计算

## 3 点简述
- 核心问题：现代微电网依赖分布式传感和通信，易受网络物理攻击威胁，需高效检测方法。
- 方法要点：在MATLAB/Simulink中构建虚拟微电网，注入多种攻击信号，使用LightGBM训练二元和多元分类模型。
- 实验或效果：多元模型准确率达99.72%，知识蒸馏后模型轻量化，实时处理延迟约54-67毫秒，适合边缘部署。

## 摘要（原文）

> Modern microgrids depend on distributed sensing and communication interfaces, making them increasingly vulnerable to cyber physical disturbances that threaten operational continuity and equipment safety. In this work, a complete virtual microgrid was designed and implemented in MATLAB/Simulink, integrating heterogeneous renewable sources and secondary controller layers. A structured cyberattack framework was developed using MGLib to inject adversarial signals directly into the secondary control pathways. Multiple attack classes were emulated, including ramp, sinusoidal, additive, coordinated stealth, and denial of service behaviors. The virtual environment was used to generate labeled datasets under both normal and attack conditions. The datasets trained Light Gradient Boosting Machine (LightGBM) models to perform two functions: detecting the presence of an intrusion (binary) and distinguishing among attack types (multiclass). The multiclass model attained 99.72% accuracy and a 99.62% F1 score, while the binary model attained 94.8% accuracy and a 94.3% F1 score. A knowledge-distillation step reduced the size of the multiclass model, allowing faster predictions with only a small drop in performance. Real-time tests showed a processing delay of about 54 to 67 ms per 1000 samples, demonstrating suitability for CPU-based edge deployment in microgrid controllers. The results confirm that lightweight machine learning based intrusion detection methods can provide fast, accurate, and efficient cyberattack detection without relying on complex deep learning models. Key contributions include: (1) development of a complete MATLAB-based virtual microgrid, (2) structured attack injection at the control layer, (3) creation of multiclass labeled datasets, and (4) design of low-cost AI models suitable for practical microgrid cybersecurity.

