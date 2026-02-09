---
layout: default
title: Optimal Turkish Subword Strategies at Scale: Systematic Evaluation of Data, Vocabulary, Morphology Interplay
---

# Optimal Turkish Subword Strategies at Scale: Systematic Evaluation of Data, Vocabulary, Morphology Interplay
**arXiv**：[2602.06942v1](https://arxiv.org/abs/2602.06942) · [PDF](https://arxiv.org/pdf/2602.06942.pdf)  
**作者**：Duygu Altinok  

**一句话要点**：提出系统评估土耳其语子词分词策略，结合词汇与数据耦合及形态学诊断工具包。

**关键词**：土耳其语分词, 形态丰富语言, 词汇数据耦合, 形态学诊断, 子词策略评估, 开源工具包

## 3 点简述
- 核心问题：土耳其语等形态丰富语言中，分词策略在词汇效率和形态保真度上的权衡挑战。
- 方法要点：首次全面研究，联合变化词汇大小和训练语料大小，比较多种分词器家族，引入形态学感知诊断工具包。
- 实验或效果：评估语义、句法和形态敏感任务，提供可操作指导，开源代码和模型。

## 摘要（原文）

> Tokenization is a pivotal design choice for neural language modeling in morphologically rich languages (MRLs) such as Turkish, where productive agglutination challenges both vocabulary efficiency and morphological fidelity. Prior studies have explored tokenizer families and vocabulary sizes but typically (i) vary vocabulary without systematically controlling the tokenizer's training corpus, (ii) provide limited intrinsic diagnostics, and (iii) evaluate a narrow slice of downstream tasks. We present the first comprehensive, principled study of Turkish subword tokenization; a "subwords manifest", that jointly varies vocabulary size and tokenizer training corpus size (data and vocabulary coupling), compares multiple tokenizer families under matched parameter budgets (WordPiece, morphology level, and character baselines), and evaluates across semantic (NLI, STS, sentiment analysis, NER), syntactic (POS, dependency parsing), and morphology-sensitive probes. To explain why tokenizers succeed or fail, we introduce a morphology-aware diagnostic toolkit that goes beyond coarse aggregates to boundary-level micro/macro F1, decoupled lemma atomicity vs. surface boundary hits, over/under-segmentation indices, character/word edit distances (CER/WER), continuation rates, and affix-type coverage and token-level atomicity. Our contributions are fourfold: (i) a systematic investigation of the vocabulary-corpus-success triad; (ii) a unified, morphology-aware evaluation framework linking intrinsic diagnostics to extrinsic outcomes; (iii) controlled comparisons identifying when character-level and morphology-level tokenization pay off; and (iv) an open-source release of evaluation code, tokenizer pipelines, and models. As the first work of its kind, this "subwords manifest" delivers actionable guidance for building effective tokenizers in MRLs and establishes a reproducible foundation for future research.

