---
layout: default
title: From Black Hole to Galaxy: Neural Operator: Framework for Accretion and Feedback Dynamics
---

# From Black Hole to Galaxy: Neural Operator: Framework for Accretion and Feedback Dynamics
**arXiv**：[2512.01576v1](https://arxiv.org/abs/2512.01576) · [PDF](https://arxiv.org/pdf/2512.01576.pdf)  
**作者**：Nihaal Bhojwani, Chuwei Wang, Hai-Yang Wang, Chang Sun, Elias R. Most, Anima Anandkumar  

**一句话要点**：提出基于神经算子的亚网格黑洞模型，以解决超大质量黑洞与宿主星系共演化模拟中的尺度分离难题。

**关键词**：神经算子, 亚网格建模, 黑洞吸积, 星系演化, 计算天体物理学, 尺度分离

## 3 点简述
- 核心问题：超大质量黑洞与星系共演化模拟因物理尺度跨越九个数量级而难以实现端到端第一性原理模拟。
- 方法要点：利用神经算子学习小尺度局部动力学，嵌入多级直接模拟中，提供边界条件和通量预测。
- 实验或效果：模型基于小域广义相对论磁流体动力学数据训练，首次捕捉吸积驱动反馈的内在变异性，实现稳定长时程模拟。

## 摘要（原文）

> Modeling how supermassive black holes co-evolve with their host galaxies is notoriously hard because the relevant physics spans nine orders of magnitude in scale-from milliparsecs to megaparsecs--making end-to-end first-principles simulation infeasible. To characterize the feedback from the small scales, existing methods employ a static subgrid scheme or one based on theoretical guesses, which usually struggle to capture the time variability and derive physically faithful results. Neural operators are a class of machine learning models that achieve significant speed-up in simulating complex dynamics. We introduce a neural-operator-based ''subgrid black hole'' that learns the small-scale local dynamics and embeds it within the direct multi-level simulations. Trained on small-domain (general relativistic) magnetohydrodynamic data, the model predicts the unresolved dynamics needed to supply boundary conditions and fluxes at coarser levels across timesteps, enabling stable long-horizon rollouts without hand-crafted closures. Thanks to the great speedup in fine-scale evolution, our approach for the first time captures intrinsic variability in accretion-driven feedback, allowing dynamic coupling between the central black hole and galaxy-scale gas. This work reframes subgrid modeling in computational astrophysics with scale separation and provides a scalable path toward data-driven closures for a broad class of systems with central accretors.

