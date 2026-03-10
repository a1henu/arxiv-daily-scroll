---
layout: default
title: Towards a more efficient bias detection in financial language models
---

# Towards a more efficient bias detection in financial language models
**arXiv**：[2603.08267v1](https://arxiv.org/abs/2603.08267) · [PDF](https://arxiv.org/pdf/2603.08267.pdf)  
**作者**：Firas Hadj Kacem, Ahmed Khanfir, Mike Papadakis  

**一句话要点**：提出跨模型引导的偏见检测方法，以降低金融语言模型偏见检测的计算成本

**关键词**：金融语言模型, 偏见检测, 计算效率, 跨模型引导, 大规模研究

## 3 点简述
- 核心问题：金融语言模型偏见检测依赖大规模突变和预测分析，计算成本高，影响实际应用部署
- 方法要点：通过分析五个模型的偏见趋势相似性，利用跨模型引导识别偏见揭示输入，减少检测所需输入对
- 实验或效果：在约17k金融新闻句子上测试，发现模型偏见率0.58%-6.05%，跨模型引导可节省高达80%计算成本

## 摘要（原文）

> Bias in financial language models constitutes a major obstacle to their adoption in real-world applications. Detecting such bias is challenging, as it requires identifying inputs whose predictions change when varying properties unrelated to the decision, such as demographic attributes. Existing approaches typically rely on exhaustive mutation and pairwise prediction analysis over large corpora, which is effective but computationally expensive-particularly for large language models and can become impractical in continuous retraining and releasing processes. Aiming at reducing this cost, we conduct a large-scale study of bias in five financial language models, examining similarities in their bias tendencies across protected attributes and exploring cross-model-guided bias detection to identify bias-revealing inputs earlier. Our study uses approximately 17k real financial news sentences, mutated to construct over 125k original-mutant pairs. Results show that all models exhibit bias under both atomic (0.58\%-6.05\%) and intersectional (0.75\%-5.97\%) settings. Moreover, we observe consistent patterns in bias-revealing inputs across models, enabling substantial reuse and cost reduction in bias detection. For example, up to 73\% of FinMA's biased behaviours can be uncovered using only 20\% of the input pairs when guided by properties derived from DistilRoBERTa outputs.

