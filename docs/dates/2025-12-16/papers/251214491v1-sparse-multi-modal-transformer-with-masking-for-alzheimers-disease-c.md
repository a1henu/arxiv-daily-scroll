---
layout: default
title: Sparse Multi-Modal Transformer with Masking for Alzheimer's Disease Classification
---

# Sparse Multi-Modal Transformer with Masking for Alzheimer's Disease Classification
**arXiv**：[2512.14491v1](https://arxiv.org/abs/2512.14491) · [PDF](https://arxiv.org/pdf/2512.14491.pdf)  
**作者**：Cheng-Han Lu, Pei-Hsuan Tsai  

**一句话要点**：提出SMMT稀疏多模态Transformer，通过聚类稀疏注意力和模态掩码提升阿尔茨海默病分类效率与鲁棒性。

**关键词**：稀疏注意力, 多模态Transformer, 阿尔茨海默病分类, 计算效率, 模态掩码, 资源感知架构

## 3 点简述
- 问题：基于Transformer的多模态系统因密集自注意力导致高计算和能耗，限制资源受限下的可扩展性。
- 方法：SMMT采用聚类稀疏注意力降低计算复杂度至近线性，并引入模态掩码增强对不完整输入的鲁棒性。
- 效果：在ADNI数据集上，SMMT保持竞争性预测性能，同时显著减少训练时间、内存使用和能耗。

## 摘要（原文）

> Transformer-based multi-modal intelligent systems often suffer from high computational and energy costs due to dense self-attention, limiting their scalability under resource constraints. This paper presents SMMT, a sparse multi-modal transformer architecture designed to improve efficiency and robustness. Building upon a cascaded multi-modal transformer framework, SMMT introduces cluster-based sparse attention to achieve near linear computational complexity and modality-wise masking to enhance robustness against incomplete inputs. The architecture is evaluated using Alzheimer's Disease classification on the ADNI dataset as a representative multi-modal case study. Experimental results show that SMMT maintains competitive predictive performance while significantly reducing training time, memory usage, and energy consumption compared to dense attention baselines, demonstrating its suitability as a resource-aware architectural component for scalable intelligent systems.

