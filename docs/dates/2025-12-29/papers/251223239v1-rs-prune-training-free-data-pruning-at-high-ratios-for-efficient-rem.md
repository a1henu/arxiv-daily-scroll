---
layout: default
title: RS-Prune: Training-Free Data Pruning at High Ratios for Efficient Remote Sensing Diffusion Foundation Models
---

# RS-Prune: Training-Free Data Pruning at High Ratios for Efficient Remote Sensing Diffusion Foundation Models
**arXiv**：[2512.23239v1](https://arxiv.org/abs/2512.23239) · [PDF](https://arxiv.org/pdf/2512.23239.pdf)  
**作者**：Fan Wei, Runmin Dong, Yushan Lai, Yixiang Yang, Zhaoyang Luo, Jinxiao Zhang, Miao Yang, Shuai Yuan, Jiyao Zhao, Bin Luo, Haohuan Fu  

**一句话要点**：提出RS-Prune训练免费数据剪枝方法，高效提升遥感扩散基础模型性能

**关键词**：遥感扩散模型, 数据剪枝, 训练免费, 场景感知聚类, 高剪枝比, 生成质量提升

## 3 点简述
- 遥感扩散基础模型面临数据冗余、噪声和类别不平衡问题，影响训练效率和收敛。
- 方法采用两阶段剪枝：基于熵去除低信息样本，再通过场景感知聚类和分层采样平衡多样性与代表性。
- 实验显示剪枝85%数据后，模型收敛和生成质量显著提升，下游任务性能达到先进水平。

## 摘要（原文）

> Diffusion-based remote sensing (RS) generative foundation models are cruial for downstream tasks. However, these models rely on large amounts of globally representative data, which often contain redundancy, noise, and class imbalance, reducing training efficiency and preventing convergence. Existing RS diffusion foundation models typically aggregate multiple classification datasets or apply simplistic deduplication, overlooking the distributional requirements of generation modeling and the heterogeneity of RS imagery. To address these limitations, we propose a training-free, two-stage data pruning approach that quickly select a high-quality subset under high pruning ratios, enabling a preliminary foundation model to converge rapidly and serve as a versatile backbone for generation, downstream fine-tuning, and other applications. Our method jointly considers local information content with global scene-level diversity and representativeness. First, an entropy-based criterion efficiently removes low-information samples. Next, leveraging RS scene classification datasets as reference benchmarks, we perform scene-aware clustering with stratified sampling to improve clustering effectiveness while reducing computational costs on large-scale unlabeled data. Finally, by balancing cluster-level uniformity and sample representativeness, the method enables fine-grained selection under high pruning ratios while preserving overall diversity and representativeness. Experiments show that, even after pruning 85\% of the training data, our method significantly improves convergence and generation quality. Furthermore, diffusion foundation models trained with our method consistently achieve state-of-the-art performance across downstream tasks, including super-resolution and semantic image synthesis. This data pruning paradigm offers practical guidance for developing RS generative foundation models.

