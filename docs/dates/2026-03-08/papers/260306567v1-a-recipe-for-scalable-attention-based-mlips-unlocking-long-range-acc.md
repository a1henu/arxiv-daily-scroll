---
layout: default
title: A recipe for scalable attention-based MLIPs: unlocking long-range accuracy with all-to-all node attention
---

# A recipe for scalable attention-based MLIPs: unlocking long-range accuracy with all-to-all node attention
**arXiv**：[2603.06567v1](https://arxiv.org/abs/2603.06567) · [PDF](https://arxiv.org/pdf/2603.06567.pdf)  
**作者**：Eric Qu, Brandon M. Wood, Aditi S. Krishnapriyan, Zachary W. Ulissi  

**一句话要点**：提出AllScAIP，一种基于注意力且能量守恒的机器学习原子间势模型，以解决大规模系统中长程相互作用准确性问题。

**关键词**：机器学习原子间势, 长程相互作用, 注意力机制, 分子动力学模拟, 能量守恒, 大规模训练

## 3 点简述
- 机器学习原子间势模型在扩展至生物分子和电解质等大系统时，难以准确捕获长程相互作用。
- AllScAIP采用数据驱动的全对全节点注意力组件，可扩展至数亿训练样本，并保持能量守恒。
- 模型在分子系统上实现最先进的能量/力精度，支持稳定长时分子动力学模拟，准确预测实验可观测值。

## 摘要（原文）

> Machine-learning interatomic potentials (MLIPs) have advanced rapidly, with many top models relying on strong physics-based inductive biases. However, as models scale to larger systems like biomolecules and electrolytes, they struggle to accurately capture long-range (LR) interactions, leading current approaches to rely on explicit physics-based terms or components. In this work, we propose AllScAIP, a straightforward, attention-based, and energy-conserving MLIP model that scales to O(100 million) training samples. It addresses the long-range challenge using an all-to-all node attention component that is data-driven. Extensive ablations reveal that in low-data/small-model regimes, inductive biases improve sample efficiency. However, as data and model size scale, these benefits diminish or even reverse, while all-to-all attention remains critical for capturing LR interactions. Our model achieves state-of-the-art energy/force accuracy on molecular systems, as well as a number of physics-based evaluations (OMol25), while being competitive on materials (OMat24) and catalysts (OC20). Furthermore, it enables stable, long-timescale MD simulations that accurately recover experimental observables, including density and heat of vaporization predictions.

