---
layout: default
title: Is BatchEnsemble a Single Model? On Calibration and Diversity of Efficient Ensembles
---

# Is BatchEnsemble a Single Model? On Calibration and Diversity of Efficient Ensembles
**arXiv**：[2601.16936v1](https://arxiv.org/abs/2601.16936) · [PDF](https://arxiv.org/pdf/2601.16936.pdf)  
**作者**：Anton Zamyatin, Patrick Indri, Sagar Malhotra, Thomas Gärtner  

**一句话要点**：揭示BatchEnsemble在资源受限场景下近似单模型，而非高效集成，影响不确定性估计。

**关键词**：不确定性估计, 高效集成, 校准性能, OOD检测, 资源受限场景

## 3 点简述
- 核心问题：资源受限场景需高效不确定性估计，但BatchEnsemble是否提供真集成效果未知。
- 方法要点：BatchEnsemble通过秩-1扰动共享网络，降低参数成本，模拟集成不确定性。
- 实验或效果：在CIFAR10等数据集上，BatchEnsemble性能接近单模型，校准和OOD检测有限。

## 摘要（原文）

> In resource-constrained and low-latency settings, uncertainty estimates must be efficiently obtained. Deep Ensembles provide robust epistemic uncertainty (EU) but require training multiple full-size models. BatchEnsemble aims to deliver ensemble-like EU at far lower parameter and memory cost by applying learned rank-1 perturbations to a shared base network. We show that BatchEnsemble not only underperforms Deep Ensembles but closely tracks a single model baseline in terms of accuracy, calibration and out-of-distribution (OOD) detection on CIFAR10/10C/SVHN. A controlled study on MNIST finds members are near-identical in function and parameter space, indicating limited capacity to realize distinct predictive modes. Thus, BatchEnsemble behaves more like a single model than a true ensemble.

