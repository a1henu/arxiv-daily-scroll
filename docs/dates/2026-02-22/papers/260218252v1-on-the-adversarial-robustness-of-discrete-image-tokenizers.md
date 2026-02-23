---
layout: default
title: On the Adversarial Robustness of Discrete Image Tokenizers
---

# On the Adversarial Robustness of Discrete Image Tokenizers
**arXiv**：[2602.18252v1](https://arxiv.org/abs/2602.18252) · [PDF](https://arxiv.org/pdf/2602.18252.pdf)  
**作者**：Rishika Bhagwatkar, Irina Rish, Nicolas Flammarion, Francesco Croce  

**一句话要点**：研究离散图像分词器的对抗鲁棒性，提出攻击与无监督对抗训练防御方法。

**关键词**：离散图像分词器, 对抗鲁棒性, 无监督对抗训练, 多模态系统, 对抗攻击

## 3 点简述
- 首次探索离散图像分词器在对抗攻击下的脆弱性，提出高效、任务无关的攻击方法。
- 基于鲁棒CLIP编码器启发，通过无监督对抗训练微调分词器，提升鲁棒性。
- 实验表明方法在分类、检索和字幕任务中有效，并能泛化到未见任务和数据。

## 摘要（原文）

> Discrete image tokenizers encode visual inputs as sequences of tokens from a finite vocabulary and are gaining popularity in multimodal systems, including encoder-only, encoder-decoder, and decoder-only models. However, unlike CLIP encoders, their vulnerability to adversarial attacks has not been explored. Ours being the first work studying this topic, we first formulate attacks that aim to perturb the features extracted by discrete tokenizers, and thus change the extracted tokens. These attacks are computationally efficient, application-agnostic, and effective across classification, multimodal retrieval, and captioning tasks. Second, to defend against this vulnerability, inspired by recent work on robust CLIP encoders, we fine-tune popular tokenizers with unsupervised adversarial training, keeping all other components frozen. While unsupervised and task-agnostic, our approach significantly improves robustness to both unsupervised and end-to-end supervised attacks and generalizes well to unseen tasks and data. Unlike supervised adversarial training, our approach can leverage unlabeled images, making it more versatile. Overall, our work highlights the critical role of tokenizer robustness in downstream tasks and presents an important step in the development of safe multimodal foundation models.

