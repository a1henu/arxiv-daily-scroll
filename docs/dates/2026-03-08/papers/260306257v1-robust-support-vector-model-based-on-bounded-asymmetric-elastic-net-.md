---
layout: default
title: Robust support vector model based on bounded asymmetric elastic net loss for binary classification
---

# Robust support vector model based on bounded asymmetric elastic net loss for binary classification
**arXiv**：[2603.06257v1](https://arxiv.org/abs/2603.06257) · [PDF](https://arxiv.org/pdf/2603.06257.pdf)  
**作者**：Haiyan Du, Hu Yang  

**一句话要点**：提出有界非对称弹性网损失函数结合SVM，以增强噪声环境下的分类鲁棒性。

**关键词**：支持向量机, 鲁棒分类, 非凸优化, 损失函数设计, 噪声处理, 几何模型

## 3 点简述
- 针对传统SVM在噪声数据和几何不合理性上的不足，提出有界非对称弹性网损失函数。
- 通过理论分析证明模型具有几何定义良好性、有界影响函数和Fisher一致性，确保鲁棒性和泛化能力。
- 设计基于裁剪对偶坐标下降的半二次算法高效求解非凸优化问题，实验显示在噪声环境中优于经典和先进SVM。

## 摘要（原文）

> In this paper, we propose a novel bounded asymmetric elastic net ($L_{baen}$) loss function and combine it with the support vector machine (SVM), resulting in the BAEN-SVM. The $L_{baen}$ is bounded and asymmetric and can degrade to the asymmetric elastic net hinge loss, pinball loss, and asymmetric least squares loss. BAEN-SVM not only effectively handles noise-contaminated data but also addresses the geometric irrationalities in the traditional SVM. By proving the violation tolerance upper bound (VTUB) of BAEN-SVM, we show that the model is geometrically well-defined. Furthermore, we derive that the influence function of BAEN-SVM is bounded, providing a theoretical guarantee of its robustness to noise. The Fisher consistency of the model further ensures its generalization capability. Since the \( L_{\text{baen}} \) loss is non-convex, we designed a clipping dual coordinate descent-based half-quadratic algorithm to solve the non-convex optimization problem efficiently. Experimental results on artificial and benchmark datasets indicate that the proposed method outperforms classical and advanced SVMs, particularly in noisy environments.

