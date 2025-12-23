---
layout: default
title: Lightweight Intrusion Detection in IoT via SHAP-Guided Feature Pruning and Knowledge-Distilled Kronecker Networks
---

# Lightweight Intrusion Detection in IoT via SHAP-Guided Feature Pruning and Knowledge-Distilled Kronecker Networks
**arXiv**：[2512.19488v1](https://arxiv.org/abs/2512.19488) · [PDF](https://arxiv.org/pdf/2512.19488.pdf)  
**作者**：Hafsa Benaddi, Mohammed Jouhari, Nouha Laamech, Anas Motii, Khalil Ibrahimi  

**一句话要点**：提出基于SHAP引导特征剪枝与知识蒸馏Kronecker网络的轻量级入侵检测系统，以解决物联网资源受限下的高精度检测需求。

**关键词**：物联网入侵检测, 特征剪枝, 知识蒸馏, Kronecker网络, 轻量级模型, 边缘计算

## 3 点简述
- 核心问题：物联网设备部署广泛，传统深度学习入侵检测系统计算量大，难以在边缘部署。
- 方法要点：结合SHAP解释性分析进行特征剪枝，并利用Kronecker结构层压缩模型，通过知识蒸馏提升泛化能力。
- 实验或效果：在TON_IoT数据集上，学生模型比教师模型小近三个数量级，宏F1分数高于0.986，推理延迟达毫秒级。

## 摘要（原文）

> The widespread deployment of Internet of Things (IoT) devices requires intrusion detection systems (IDS) with high accuracy while operating under strict resource constraints. Conventional deep learning IDS are often too large and computationally intensive for edge deployment. We propose a lightweight IDS that combines SHAP-guided feature pruning with knowledge-distilled Kronecker networks. A high-capacity teacher model identifies the most relevant features through SHAP explanations, and a compressed student leverages Kronecker-structured layers to minimize parameters while preserving discriminative inputs. Knowledge distillation transfers softened decision boundaries from teacher to student, improving generalization under compression. Experiments on the TON\_IoT dataset show that the student is nearly three orders of magnitude smaller than the teacher yet sustains macro-F1 above 0.986 with millisecond-level inference latency. The results demonstrate that explainability-driven pruning and structured compression can jointly enable scalable, low-latency, and energy-efficient IDS for heterogeneous IoT environments.

