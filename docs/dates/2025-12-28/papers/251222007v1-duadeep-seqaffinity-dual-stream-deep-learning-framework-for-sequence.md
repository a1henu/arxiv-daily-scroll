---
layout: default
title: DuaDeep-SeqAffinity: Dual-Stream Deep Learning Framework for Sequence-Only Antigen-Antibody Affinity Prediction
---

# DuaDeep-SeqAffinity: Dual-Stream Deep Learning Framework for Sequence-Only Antigen-Antibody Affinity Prediction
**arXiv**：[2512.22007v1](https://arxiv.org/abs/2512.22007) · [PDF](https://arxiv.org/pdf/2512.22007.pdf)  
**作者**：Aicha Boutorh, Soumia Bouyahiaoui, Sara Belhadj, Nour El Yakine Guendouz, Manel Kara Laouar  

**一句话要点**：提出DuaDeep-SeqAffinity双流深度学习框架，仅基于序列预测抗原-抗体亲和力，加速药物发现。

**关键词**：抗原-抗体亲和力预测, 序列深度学习, 双流架构, 蛋白质语言模型, 高通量筛选, 药物发现

## 3 点简述
- 核心问题：传统方法依赖稀缺的3D结构，计算成本高，限制了亲和力预测的效率和可扩展性。
- 方法要点：使用ESM-2预训练嵌入，结合1D CNN检测局部基序和Transformer编码器捕获全局上下文，通过融合模块整合特征进行回归。
- 实验或效果：在实验中显著优于单分支变体和现有SOTA方法，Pearson相关0.688，AUC 0.890，证明序列嵌入可替代结构建模。

## 摘要（原文）

> Predicting the binding affinity between antigens and antibodies is fundamental to drug discovery and vaccine development. Traditional computational approaches often rely on experimentally determined 3D structures, which are scarce and computationally expensive to obtain. This paper introduces DuaDeep-SeqAffinity, a novel sequence-only deep learning framework that predicts affinity scores solely from their amino acid sequences using a dual-stream hybrid architecture. Our approach leverages pre-trained ESM-2 protein language model embeddings, combining 1D Convolutional Neural Networks (CNNs) for local motif detection with Transformer encoders for global contextual representation. A subsequent fusion module integrates these multi-faceted features, which are then passed to a fully connected network for final score regression. Experimental results demonstrate that DuaDeep-SeqAffinity significantly outperforms individual architectural components and existing state-of-the-art (SOTA) methods. DuaDeep achieved a superior Pearson correlation of 0.688, an R^2 of 0.460, and a Root Mean Square Error (RMSE) of 0.737, surpassing single-branch variants ESM-CNN and ESM-Transformer. Notably, the model achieved an Area Under the Curve (AUC) of 0.890, outperforming sequence-only benchmarks and even surpassing structure-sequence hybrid models. These findings prove that high-fidelity sequence embeddings can capture essential binding patterns typically reserved for structural modeling. By eliminating the reliance on 3D structures, DuaDeep-SeqAffinity provides a highly scalable and efficient solution for high-throughput screening of vast sequence libraries, significantly accelerating the therapeutic discovery pipeline.

