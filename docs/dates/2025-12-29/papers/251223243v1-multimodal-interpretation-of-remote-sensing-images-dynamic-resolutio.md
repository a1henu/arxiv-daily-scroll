---
layout: default
title: Multimodal Interpretation of Remote Sensing Images: Dynamic Resolution Input Strategy and Multi-scale Vision-Language Alignment Mechanism
---

# Multimodal Interpretation of Remote Sensing Images: Dynamic Resolution Input Strategy and Multi-scale Vision-Language Alignment Mechanism
**arXiv**：[2512.23243v1](https://arxiv.org/abs/2512.23243) · [PDF](https://arxiv.org/pdf/2512.23243.pdf)  
**作者**：Siyu Zhang, Ying Chen, Lianlei Shan, Runhe Qiu  

**一句话要点**：提出动态分辨率输入策略与多尺度视觉-语言对齐机制，以提升遥感图像多模态融合的准确性与效率。

**关键词**：遥感图像多模态融合, 动态分辨率输入, 多尺度视觉-语言对齐, 图像描述, 跨模态检索, 计算效率优化

## 3 点简述
- 针对固定分辨率无法平衡效率与细节、单尺度对齐缺乏语义层次的问题。
- 采用动态分辨率输入策略自适应分配计算资源，构建多尺度视觉-语言对齐机制捕获跨模态语义一致性。
- 在RS-GPT4V数据集上，图像描述和跨模态检索任务中BLEU-4、CIDEr和R@10指标表现优于传统方法。

## 摘要（原文）

> Multimodal fusion of remote sensing images serves as a core technology for overcoming the limitations of single-source data and improving the accuracy of surface information extraction, which exhibits significant application value in fields such as environmental monitoring and urban planning. To address the deficiencies of existing methods, including the failure of fixed resolutions to balance efficiency and detail, as well as the lack of semantic hierarchy in single-scale alignment, this study proposes a Vision-language Model (VLM) framework integrated with two key innovations: the Dynamic Resolution Input Strategy (DRIS) and the Multi-scale Vision-language Alignment Mechanism (MS-VLAM).Specifically, the DRIS adopts a coarse-to-fine approach to adaptively allocate computational resources according to the complexity of image content, thereby preserving key fine-grained features while reducing redundant computational overhead. The MS-VLAM constructs a three-tier alignment mechanism covering object, local-region and global levels, which systematically captures cross-modal semantic consistency and alleviates issues of semantic misalignment and granularity imbalance.Experimental results on the RS-GPT4V dataset demonstrate that the proposed framework significantly improves the accuracy of semantic understanding and computational efficiency in tasks including image captioning and cross-modal retrieval. Compared with conventional methods, it achieves superior performance in evaluation metrics such as BLEU-4 and CIDEr for image captioning, as well as R@10 for cross-modal retrieval. This technical framework provides a novel approach for constructing efficient and robust multimodal remote sensing systems, laying a theoretical foundation and offering technical guidance for the engineering application of intelligent remote sensing interpretation.

