---
layout: default
title: BackdoorVLM: A Benchmark for Backdoor Attacks on Vision-Language Models
---

# BackdoorVLM: A Benchmark for Backdoor Attacks on Vision-Language Models
**arXiv**：[2511.18921v1](https://arxiv.org/abs/2511.18921) · [PDF](https://arxiv.org/pdf/2511.18921.pdf)  
**作者**：Juncheng Li, Yige Li, Hanxun Huang, Yunhao Chen, Xin Wang, Yixu Wang, Xingjun Ma, Yu-Gang Jiang  

**一句话要点**：提出BackdoorVLM基准以评估视觉语言模型中的后门攻击

**关键词**：后门攻击, 视觉语言模型, 多模态基准, 文本触发, 模型安全

## 3 点简述
- 核心问题：多模态基础模型中的后门攻击威胁尚未充分探索，影响模型可靠性。
- 方法要点：构建统一基准，涵盖5类后门威胁，包括目标拒绝和恶意注入等。
- 实验或效果：在12种攻击方法上测试，文本触发主导，1%投毒率可达90%成功率。

## 摘要（原文）

> Backdoor attacks undermine the reliability and trustworthiness of machine learning systems by injecting hidden behaviors that can be maliciously activated at inference time. While such threats have been extensively studied in unimodal settings, their impact on multimodal foundation models, particularly vision-language models (VLMs), remains largely underexplored. In this work, we introduce \textbf{BackdoorVLM}, the first comprehensive benchmark for systematically evaluating backdoor attacks on VLMs across a broad range of settings. It adopts a unified perspective that injects and analyzes backdoors across core vision-language tasks, including image captioning and visual question answering. BackdoorVLM organizes multimodal backdoor threats into 5 representative categories: targeted refusal, malicious injection, jailbreak, concept substitution, and perceptual hijack. Each category captures a distinct pathway through which an adversary can manipulate a model's behavior. We evaluate these threats using 12 representative attack methods spanning text, image, and bimodal triggers, tested on 2 open-source VLMs and 3 multimodal datasets. Our analysis reveals that VLMs exhibit strong sensitivity to textual instructions, and in bimodal backdoors the text trigger typically overwhelms the image trigger when forming the backdoor mapping. Notably, backdoors involving the textual modality remain highly potent, with poisoning rates as low as 1\% yielding over 90\% success across most tasks. These findings highlight significant, previously underexplored vulnerabilities in current VLMs. We hope that BackdoorVLM can serve as a useful benchmark for analyzing and mitigating multimodal backdoor threats. Code is available at: https://github.com/bin015/BackdoorVLM .

