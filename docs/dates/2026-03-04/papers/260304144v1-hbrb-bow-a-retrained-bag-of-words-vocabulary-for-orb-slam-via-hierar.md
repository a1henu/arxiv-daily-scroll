---
layout: default
title: HBRB-BoW: A Retrained Bag-of-Words Vocabulary for ORB-SLAM via Hierarchical BRB-KMeans
---

# HBRB-BoW: A Retrained Bag-of-Words Vocabulary for ORB-SLAM via Hierarchical BRB-KMeans
**arXiv**：[2603.04144v1](https://arxiv.org/abs/2603.04144) · [PDF](https://arxiv.org/pdf/2603.04144.pdf)  
**作者**：Minjae Lee, Sang-Min Choi, Gun-Woo Kim, Suwon Lee  

**一句话要点**：提出HBRB-BoW词汇训练算法以提升ORB-SLAM在复杂环境中的视觉词汇质量

**关键词**：视觉SLAM, 词汇训练, 分层聚类, ORB-SLAM, 闭环检测, 重定位

## 3 点简述
- ORB-SLAM的二进制词汇因传统聚类方法导致特征分布表示不精确，影响系统性能
- 通过分层聚类中集成全局实值流，在叶节点进行最终二值化，保留高保真描述符信息
- 实验表明该方法生成更具区分性和结构化的词汇，预期改善闭环检测和重定位任务

## 摘要（原文）

> In visual simultaneous localization and mapping (SLAM), the quality of the visual vocabulary is fundamental to the system's ability to represent environments and recognize locations. While ORB-SLAM is a widely used framework, its binary vocabulary, trained through the k-majority-based bag-of-words (BoW) approach, suffers from inherent precision loss. The inability of conventional binary clustering to represent subtle feature distributions leads to the degradation of visual words, a problem that is compounded as errors accumulate and propagate through the hierarchical tree structure. To address these structural deficiencies, this paper proposes hierarchical binary-to-real-and-back (HBRB)-BoW, a refined hierarchical binary vocabulary training algorithm. By integrating a global real-valued flow within the hierarchical clustering process, our method preserves high-fidelity descriptor information until the final binarization at the leaf nodes. Experimental results demonstrate that the proposed approach yields a more discriminative and well-structured vocabulary than traditional methods, significantly enhancing the representational integrity of the visual dictionary in complex environments. Furthermore, replacing the default ORB-SLAM vocabulary file with our HBRB-BoW file is expected to improve performance in loop closing and relocalization tasks.

