---
layout: default
title: Subspace Alignment for Vision-Language Model Test-time Adaptation
---

# Subspace Alignment for Vision-Language Model Test-time Adaptation
**arXiv**：[2601.08139v1](https://arxiv.org/abs/2601.08139) · [PDF](https://arxiv.org/pdf/2601.08139.pdf)  
**作者**：Zhichen Zeng, Wenxuan Bao, Xiao Lin, Ruizhong Qiu, Tianxin Wei, Xuying Ning, Yuchen Yan, Chen Luo, Monica Xiao Cheng, Jingrui He, Hanghang Tong  

**一句话要点**：提出SubTTA方法，通过子空间对齐增强视觉语言模型在测试时适应中的零样本预测可靠性。

**关键词**：视觉语言模型, 测试时适应, 子空间对齐, 模态差距, 视觉噪声过滤, 零样本预测

## 3 点简述
- 核心问题：分布偏移导致视觉与文本模态间存在差距，且视觉嵌入包含任务无关噪声，影响零样本预测准确性。
- 方法要点：提取并对齐模态的主子空间以弥合模态差距，并投影视觉特征到任务特定文本子空间以过滤噪声。
- 实验或效果：在多个基准和VLM架构上验证，平均性能提升2.24%，优于现有TTA方法。

## 摘要（原文）

> Vision-language models (VLMs), despite their extraordinary zero-shot capabilities, are vulnerable to distribution shifts. Test-time adaptation (TTA) emerges as a predominant strategy to adapt VLMs to unlabeled test data on the fly. However, existing TTA methods heavily rely on zero-shot predictions as pseudo-labels for self-training, which can be unreliable under distribution shifts and misguide adaptation due to two fundamental limitations. First (Modality Gap), distribution shifts induce gaps between visual and textual modalities, making cross-modal relations inaccurate. Second (Visual Nuisance), visual embeddings encode rich but task-irrelevant noise that often overwhelms task-specific semantics under distribution shifts. To address these limitations, we propose SubTTA, which aligns the semantic subspaces of both modalities to enhance zero-shot predictions to better guide the TTA process. To bridge the modality gap, SubTTA extracts the principal subspaces of both modalities and aligns the visual manifold to the textual semantic anchor by minimizing their chordal distance. To eliminate visual nuisance, SubTTA projects the aligned visual features onto the task-specific textual subspace, which filters out task-irrelevant noise by constraining visual embeddings within the valid semantic span, and standard TTA is further performed on the purified space to refine the decision boundaries. Extensive experiments on various benchmarks and VLM architectures demonstrate the effectiveness of SubTTA, yielding an average improvement of 2.24% over state-of-the-art TTA methods.

