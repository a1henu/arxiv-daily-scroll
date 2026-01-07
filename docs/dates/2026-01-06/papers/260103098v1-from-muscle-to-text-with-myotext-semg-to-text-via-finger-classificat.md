---
layout: default
title: From Muscle to Text with MyoText: sEMG to Text via Finger Classification and Transformer-Based Decoding
---

# From Muscle to Text with MyoText: sEMG to Text via Finger Classification and Transformer-Based Decoding
**arXiv**：[2601.03098v1](https://arxiv.org/abs/2601.03098) · [PDF](https://arxiv.org/pdf/2601.03098.pdf)  
**作者**：Meghna Roy Chowdhury, Shreyas Sen, Yi Ding  

**一句话要点**：提出MyoText框架，通过手指分类与Transformer解码实现sEMG到文本的转换，用于无键盘输入场景。

**关键词**：表面肌电信号解码, 手指分类, Transformer解码, 无键盘输入, 可穿戴系统

## 3 点简述
- 核心问题：如何从表面肌电信号（sEMG）解码文本，支持可穿戴和混合现实系统的无键盘输入。
- 方法要点：采用分层框架，先分类手指激活，再推断字母，最后用T5 Transformer重建句子。
- 实验或效果：在30用户数据集上，手指分类准确率85.4%，字符错误率5.4%，词错误率6.5%。

## 摘要（原文）

> Surface electromyography (sEMG) provides a direct neural interface for decoding muscle activity and offers a promising foundation for keyboard-free text input in wearable and mixed-reality systems. Previous sEMG-to-text studies mainly focused on recognizing letters directly from sEMG signals, forming an important first step toward translating muscle activity into text. Building on this foundation, we present MyoText, a hierarchical framework that decodes sEMG signals to text through physiologically grounded intermediate stages. MyoText first classifies finger activations from multichannel sEMG using a CNN-BiLSTM-Attention model, applies ergonomic typing priors to infer letters, and reconstructs full sentences with a fine-tuned T5 transformer. This modular design mirrors the natural hierarchy of typing, linking muscle intent to language output and reducing the search space for decoding. Evaluated on 30 users from the emg2qwerty dataset, MyoText outperforms baselines by achieving 85.4% finger-classification accuracy, 5.4% character error rate (CER), and 6.5% word error rate (WER). Beyond accuracy gains, this methodology establishes a principled pathway from neuromuscular signals to text, providing a blueprint for virtual and augmented-reality typing interfaces that operate entirely without physical keyboards. By integrating ergonomic structure with transformer-based linguistic reasoning, MyoText advances the feasibility of seamless, wearable neural input for future ubiquitous computing environments.

