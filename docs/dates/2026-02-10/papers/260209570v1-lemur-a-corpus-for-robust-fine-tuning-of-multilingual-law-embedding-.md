---
layout: default
title: LEMUR: A Corpus for Robust Fine-Tuning of Multilingual Law Embedding Models for Retrieval
---

# LEMUR: A Corpus for Robust Fine-Tuning of Multilingual Law Embedding Models for Retrieval
**arXiv**：[2602.09570v1](https://arxiv.org/abs/2602.09570) · [PDF](https://arxiv.org/pdf/2602.09570.pdf)  
**作者**：Narges Baba Ahmadi, Jan Strich, Martin Semmann, Chris Biemann  

**一句话要点**：提出LEMUR多语言法律语料库，通过对比学习微调嵌入模型以提升法律检索的鲁棒性。

**关键词**：多语言法律检索, 嵌入模型微调, 对比学习, 法律语料库, PDF文本提取, 跨语言评估

## 3 点简述
- 问题：多语言法律检索中，LLMs因缺乏领域适配嵌入模型和PDF文本提取噪声而受限。
- 方法：构建基于EUR-Lex的LEMUR语料库，量化PDF转换保真度，并用对比目标微调多语言嵌入模型。
- 效果：微调显著提升高低资源语言的检索准确率，跨语言评估显示改进可迁移至未见语言。

## 摘要（原文）

> Large language models (LLMs) are increasingly used to access legal information. Yet, their deployment in multilingual legal settings is constrained by unreliable retrieval and the lack of domain-adapted, open-embedding models. In particular, existing multilingual legal corpora are not designed for semantic retrieval, and PDF-based legislative sources introduce substantial noise due to imperfect text extraction. To address these challenges, we introduce LEMUR, a large-scale multilingual corpus of EU environmental legislation constructed from 24,953 official EUR-Lex PDF documents covering 25 languages. We quantify the fidelity of PDF-to-text conversion by measuring lexical consistency against authoritative HTML versions using the Lexical Content Score (LCS). Building on LEMUR, we fine-tune three state-of-the-art multilingual embedding models using contrastive objectives in both monolingual and bilingual settings, reflecting realistic legal-retrieval scenarios. Experiments across low- and high-resource languages demonstrate that legal-domain fine-tuning consistently improves Top-k retrieval accuracy relative to strong baselines, with particularly pronounced gains for low-resource languages. Cross-lingual evaluations show that these improvements transfer to unseen languages, indicating that fine-tuning primarily enhances language-independent, content-level legal representations rather than language-specific cues. We publish code\footnote{\href{https://github.com/nargesbh/eur_lex}{GitHub Repository}} and data\footnote{\href{https://huggingface.co/datasets/G4KMU/LEMUR}{Hugging Face Dataset}}.

