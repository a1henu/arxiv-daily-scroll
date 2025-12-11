---
layout: default
title: Sequential Testing for Descriptor-Agnostic LiDAR Loop Closure in Repetitive Environments
---

# Sequential Testing for Descriptor-Agnostic LiDAR Loop Closure in Repetitive Environments
**arXiv**：[2512.09447v1](https://arxiv.org/abs/2512.09447) · [PDF](https://arxiv.org/pdf/2512.09447.pdf)  
**作者**：Jaehyun Kim, Seungwon Choi, Tae-Wan Kim  

**一句话要点**：提出基于截断序贯概率比检验的LiDAR闭环验证方法，以抑制重复环境中的误检。

**关键词**：LiDAR闭环检测, 序贯概率比检验, 重复环境, 多帧验证, 描述符无关

## 3 点简述
- 核心问题：LiDAR闭环在结构重复室内环境中易产生误检，现有方法依赖单帧描述符比较或固定阈值。
- 方法要点：采用多帧描述符相似性流，通过序贯概率比检验自适应决策，优先控制错误率。
- 实验或效果：在五序列数据集上评估，相比基线方法，该方法提升精度并减少闭环混淆影响。

## 摘要（原文）

> We propose a descriptor-agnostic, multi-frame loop closure verification method that formulates LiDAR loop closure as a truncated Sequential Probability Ratio Test (SPRT). Instead of deciding from a single descriptor comparison or using fixed thresholds with late-stage Iterative Closest Point (ICP) vetting, the verifier accumulates a short temporal stream of descriptor similarities between a query and each candidate. It then issues an accept/reject decision adaptively once sufficient multi-frame evidence has been observed, according to user-specified Type-I/II error design targets. This precision-first policy is designed to suppress false positives in structurally repetitive indoor environments. We evaluate the verifier on a five-sequence library dataset, using a fixed retrieval front-end with several representative LiDAR global descriptors. Performance is assessed via segment-level K-hit precision-recall and absolute trajectory error (ATE) and relative pose error (RPE) after pose graph optimization. Across descriptors, the sequential verifier consistently improves precision and reduces the impact of aliased loops compared with single-frame and heuristic multi-frame baselines. Our implementation and dataset will be released at: https://github.com/wanderingcar/snu_library_dataset.

