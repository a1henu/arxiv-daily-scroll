---
layout: default
title: Multi-Modal LLM based Image Captioning in ICT: Bridging the Gap Between General and Industry Domain
---

# Multi-Modal LLM based Image Captioning in ICT: Bridging the Gap Between General and Industry Domain
**arXiv**：[2601.09298v1](https://arxiv.org/abs/2601.09298) · [PDF](https://arxiv.org/pdf/2601.09298.pdf)  
**作者**：Lianying Chao, Haoran Cai, Xubin Li, Kai Zhang, Sijie Wu, Rui Xu  

**一句话要点**：提出多阶段渐进训练策略，在ICT领域构建领域特定图像描述模型以解决多模态知识提取问题。

**关键词**：多模态大模型, 图像描述, 领域特定训练, 渐进训练策略, ICT领域应用, 监督微调

## 3 点简述
- 核心问题：ICT领域图像模态知识难以提取，传统方法无图像描述能力，多模态大模型缺乏领域知识。
- 方法要点：采用三阶段渐进训练，包括合成数据监督微调、专家标注微调和指令微调，构建领域特定图像描述模型。
- 实验或效果：模型仅7B参数，在BLEU指标上优于32B参数SOTA模型，在ICT专家构建的客观题上准确率超过Qwen2.5-VL 32B。

## 摘要（原文）

> In the information and communications technology (ICT) industry, training a domain-specific large language model (LLM) or constructing a retrieval-augmented generation system requires a substantial amount of high-value domain knowledge. However, the knowledge is not only hidden in the textual modality but also in the image modality. Traditional methods can parse text from domain documents but dont have image captioning ability. Multi-modal LLM (MLLM) can understand images, but they do not have sufficient domain knowledge. To address the above issues, this paper proposes a multi-stage progressive training strategy to train a Domain-specific Image Captioning Model (DICModel) in ICT, and constructs a standard evaluation system to validate the performance of DICModel. Specifically, this work first synthesizes about 7K image-text pairs by combining the Mermaid tool and LLMs, which are used for the first-stage supervised-fine-tuning (SFT) of DICModel. Then, ICT-domain experts manually annotate about 2K image-text pairs for the second-stage SFT of DICModel. Finally, experts and LLMs jointly synthesize about 1.5K visual question answering data for the instruction-based SFT. Experimental results indicate that our DICModel with only 7B parameters performs better than other state-of-the-art models with 32B parameters. Compared to the SOTA models with 7B and 32B parameters, our DICModel increases the BLEU metric by approximately 56.8% and 20.8%, respectively. On the objective questions constructed by ICT domain experts, our DICModel outperforms Qwen2.5-VL 32B by 1% in terms of accuracy rate. In summary, this work can efficiently and accurately extract the logical text from images, which is expected to promote the development of multimodal models in the ICT domain.

