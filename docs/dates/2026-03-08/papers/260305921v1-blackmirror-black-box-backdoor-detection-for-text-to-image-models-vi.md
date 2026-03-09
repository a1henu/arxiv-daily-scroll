---
layout: default
title: BlackMirror: Black-Box Backdoor Detection for Text-to-Image Models via Instruction-Response Deviation
---

# BlackMirror: Black-Box Backdoor Detection for Text-to-Image Models via Instruction-Response Deviation
**arXiv**：[2603.05921v1](https://arxiv.org/abs/2603.05921) · [PDF](https://arxiv.org/pdf/2603.05921.pdf)  
**作者**：Feiran Li, Qianqian Xu, Shilong Bao, Zhiyong Yang, Xilin Zhao, Xiaochun Cao, Qingming Huang  

**一句话要点**：提出BlackMirror框架以解决黑盒文本到图像模型后门检测问题

**关键词**：后门检测, 文本到图像模型, 黑盒设置, 语义偏差, 即插即用框架, 模型即服务

## 3 点简述
- 核心问题：黑盒设置下检测后门文本到图像模型，现有方法难以应对视觉多样化的后门攻击
- 方法要点：基于语义模式稳定操纵的观察，通过MirrorMatch对齐视觉与指令检测偏差，MirrorVerify评估偏差稳定性
- 实验或效果：在广泛攻击中实现准确检测，无需训练，可作为即插即用模块部署于MaaS应用

## 摘要（原文）

> This paper investigates the challenging task of detecting backdoored text-to-image models under black-box settings and introduces a novel detection framework BlackMirror. Existing approaches typically rely on analyzing image-level similarity, under the assumption that backdoor-triggered generations exhibit strong consistency across samples. However, they struggle to generalize to recently emerging backdoor attacks, where backdoored generations can appear visually diverse. BlackMirror is motivated by an observation: across backdoor attacks, {only partial semantic patterns within the generated image are steadily manipulated, while the rest of the content remains diverse or benign. Accordingly, BlackMirror consists of two components: MirrorMatch, which aligns visual patterns with the corresponding instructions to detect semantic deviations; and MirrorVerify, which evaluates the stability of these deviations across varied prompts to distinguish true backdoor behavior from benign responses. BlackMirror is a general, training-free framework that can be deployed as a plug-and-play module in Model-as-a-Service (MaaS) applications. Comprehensive experiments demonstrate that BlackMirror achieves accurate detection across a wide range of attacks. Code is available at https://github.com/Ferry-Li/BlackMirror.

