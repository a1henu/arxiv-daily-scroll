---
layout: default
title: TRIZ-RAGNER: A Retrieval-Augmented Large Language Model for TRIZ-Aware Named Entity Recognition in Patent-Based Contradiction Mining
---

# TRIZ-RAGNER: A Retrieval-Augmented Large Language Model for TRIZ-Aware Named Entity Recognition in Patent-Based Contradiction Mining
**arXiv**：[2602.23656v1](https://arxiv.org/abs/2602.23656) · [PDF](https://arxiv.org/pdf/2602.23656.pdf)  
**作者**：Zitong Xu, Yuqing Wu, Yue Zhao  

**一句话要点**：提出TRIZ-RAGNER框架，通过检索增强LLM解决专利矛盾挖掘中TRIZ参数提取的语义模糊与幻觉问题。

**关键词**：专利分析, 矛盾挖掘, 命名实体识别, 检索增强生成, 大语言模型, TRIZ理论

## 3 点简述
- 核心问题：现有方法依赖规则或传统模型，处理复杂专利语言时存在语义模糊、领域依赖和泛化能力不足。
- 方法要点：将矛盾挖掘重构为语义级NER任务，集成密集检索、交叉编码器重排序和结构化提示，注入TRIZ知识。
- 实验或效果：在PaTRIZ数据集上，F1分数达84.2%，比最强基线提升7.3个百分点，验证了检索增强知识接地的有效性。

## 摘要（原文）

> TRIZ-based contradiction mining is a fundamental task in patent analysis and systematic innovation, as it enables the identification of improving and worsening technical parameters that drive inventive problem solving. However, existing approaches largely rely on rule-based systems or traditional machine learning models, which struggle with semantic ambiguity, domain dependency, and limited generalization when processing complex patent language. Recently, large language models (LLMs) have shown strong semantic understanding capabilities, yet their direct application to TRIZ parameter extraction remains challenging due to hallucination and insufficient grounding in structured TRIZ knowledge. To address these limitations, this paper proposes TRIZ-RAGNER, a retrieval-augmented large language model framework for TRIZ-aware named entity recognition in patent-based contradiction mining. TRIZ-RAGNER reformulates contradiction mining as a semantic-level NER task and integrates dense retrieval over a TRIZ knowledge base, cross-encoder reranking for context refinement, and structured LLM prompting to extract improving and worsening parameters from patent sentences. By injecting domain-specific TRIZ knowledge into the LLM reasoning process, the proposed framework effectively reduces semantic noise and improves extraction consistency. Experiments on the PaTRIZ dataset demonstrate that TRIZ-RAGNER consistently outperforms traditional sequence labeling models and LLM-based baselines. The proposed framework achieves a precision of 85.6%, a recall of 82.9%, and an F1-score of 84.2% in TRIZ contradiction pair identification. Compared with the strongest baseline using prompt-enhanced GPT, TRIZ-RAGNER yields an absolute F1-score improvement of 7.3 percentage points, confirming the effectiveness of retrieval-augmented TRIZ knowledge grounding for robust and accurate patent-based contradiction mining.

