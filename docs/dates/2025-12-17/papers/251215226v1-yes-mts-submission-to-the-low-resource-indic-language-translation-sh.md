---
layout: default
title: Yes-MT's Submission to the Low-Resource Indic Language Translation Shared Task in WMT 2024
---

# Yes-MT's Submission to the Low-Resource Indic Language Translation Shared Task in WMT 2024
**arXiv**：[2512.15226v1](https://arxiv.org/abs/2512.15226) · [PDF](https://arxiv.org/pdf/2512.15226.pdf)  
**作者**：Yash Bhaskar, Parameswari Krishnamurthy  

**一句话要点**：提出多种方法用于WMT 2024低资源印度语言翻译任务，包括微调预训练模型和LLM提示。

**关键词**：低资源机器翻译, 印度语言翻译, 预训练模型微调, 大型语言模型提示, LoRA微调, Transformer模型

## 3 点简述
- 核心问题：低资源印度语言（如阿萨姆语、米佐语）与英语之间的翻译挑战。
- 方法要点：探索了mT5、IndicBart微调、LoRA微调IndicTrans2、LLM零/少样本提示及Transformer从头训练。
- 实验或效果：在WMT23测试数据上使用SacreBLEU和CHRF评估，突显低资源翻译难点及LLM微调潜力。

## 摘要（原文）

> This paper presents the systems submitted by the Yes-MT team for the Low-Resource Indic Language Translation Shared Task at WMT 2024 (Pakray et al., 2024), focusing on translating between English and the Assamese, Mizo, Khasi, and Manipuri languages. The experiments explored various approaches, including fine-tuning pre-trained models like mT5 (Xue et al., 2020) and IndicBart (Dabre et al., 2021) in both multilingual and monolingual settings, LoRA (Hu et al., 2021) fine-tuning IndicTrans2 (Gala et al., 2023), zero-shot and few-shot prompting (Brown, 2020) with large language models (LLMs) like Llama 3 (Dubey et al., 2024) and Mixtral 8x7b (Jiang et al., 2024), LoRA supervised fine-tuning of Llama 3 (Mecklenburg et al., 2024), and training Transformer models (Vaswani, 2017) from scratch. The results were evaluated on the WMT23 Low-Resource Indic Language Translation Shared Task test data using SacreBLEU (Post, 2018) and CHRF (Popovic, 2015), highlighting the challenges of low-resource translation and the potential of LLMs for these tasks, particularly with fine-tuning.

