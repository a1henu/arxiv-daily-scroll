---
layout: default
title: EvalQReason: A Framework for Step-Level Reasoning Evaluation in Large Language Models
---

# EvalQReason: A Framework for Step-Level Reasoning Evaluation in Large Language Models
**arXiv**：[2602.02295v1](https://arxiv.org/abs/2602.02295) · [PDF](https://arxiv.org/pdf/2602.02295.pdf)  
**作者**：Shaima Ahmad Freja, Ferhat Ozgur Catak, Betul Yurdem, Chunming Rong  

**一句话要点**：提出EvalQReason框架，通过步骤级概率分布分析评估大语言模型推理质量，无需人工标注。

**关键词**：大语言模型评估, 推理质量量化, 步骤级分析, 概率分布, 无监督评估, 领域特异性

## 3 点简述
- 核心问题：现有方法侧重最终答案正确性，难以系统评估大语言模型内部推理过程。
- 方法要点：引入连续步骤差异和步骤到最终收敛算法，使用统计指标量化推理动态。
- 实验效果：在数学和医学数据集上验证，基于连续步骤差异的特征在正确性分类中表现优异，推理动态具有领域特异性。

## 摘要（原文）

> Large Language Models (LLMs) are increasingly deployed in critical applications requiring reliable reasoning, yet their internal reasoning processes remain difficult to evaluate systematically. Existing methods focus on final-answer correctness, providing limited insight into how reasoning unfolds across intermediate steps. We present EvalQReason, a framework that quantifies LLM reasoning quality through step-level probability distribution analysis without requiring human annotation. The framework introduces two complementary algorithms: Consecutive Step Divergence (CSD), which measures local coherence between adjacent reasoning steps, and Step-to-Final Convergence (SFC), which assesses global alignment with final answers. Each algorithm employs five statistical metrics to capture reasoning dynamics. Experiments across mathematical and medical datasets with open-source 7B-parameter models demonstrate that CSD-based features achieve strong predictive performance for correctness classification, with classical machine learning models reaching F1=0.78 and ROC-AUC=0.82, and sequential neural models substantially improving performance (F1=0.88, ROC-AUC=0.97). CSD consistently outperforms SFC, and sequential architectures outperform classical machine learning approaches. Critically, reasoning dynamics prove domain-specific: mathematical reasoning exhibits clear divergence-based discrimination patterns between correct and incorrect solutions, while medical reasoning shows minimal discriminative signals, revealing fundamental differences in how LLMs process different reasoning types. EvalQReason enables scalable, process-aware evaluation of reasoning reliability, establishing probability-based divergence analysis as a principled approach for trustworthy AI deployment.

